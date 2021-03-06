import pandas as pd
import numpy as np
import math
import operator
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 수정계획 1 : 상위 한개의 장르만 추출하는데 그게 아니라 상위 3개의 장르를 뽑아
#             그 중 선택한 장르와 가장 상관관계가 높은 장르를 추천하는 것을 어떨까?
class ModelFirst:
    def model1(self, selected_genres):
        df = pd.read_csv('pages/AImodels/user_pref.csv')
        corr = np.load('pages/AImodels/corr_save.npy')
        user_pref = df.to_numpy()
        transformer = StandardScaler()
        transformer.fit(user_pref)
        standard_user_pref = transformer.transform(user_pref)
        df = pd.DataFrame(user_pref, columns=df.columns)
        
        first_genre_index = df[selected_genres[0]].sort_values(ascending=False).head(1400).index
        second_genre_index = df[selected_genres[1]].sort_values(ascending=False).head(1400).index
        
        common_index = []
        for idx in first_genre_index:
            if idx in second_genre_index:
                common_index.append(idx)

        common_df = pd.DataFrame(index=range(0,len(common_index)), columns=df.columns)
        i = 0
        for idx in common_index:
            common_df.iloc[i] = df.iloc[idx]
            i = i + 1

        genre_title = df.columns
        genre_list = list(genre_title)
        first_idx = genre_list.index(selected_genres[0])
        second_idx = genre_list.index(selected_genres[1])
        co1 = corr[first_idx]
        co2 = corr[second_idx]

        select_values = common_df.values

        pred1 = (select_values * co1) / np.array([np.abs(co1).sum(axis=0)])
        pred1_df = pd.DataFrame(pred1, index=common_df.index, columns = common_df.columns)
        index = common_df.index
        result_dict = {}
        for i in index:
            sorted_tuple = pred1_df.iloc[i].sort_values(ascending=False)
            for genre in sorted_tuple.head(5).index.tolist():
                if genre not in result_dict and genre not in selected_genres:
                    result_dict[genre] = 0
                if genre not in selected_genres:
                    result_dict[genre] += 1
        sorted_result_dict = sorted(result_dict.items(), key=operator.itemgetter(1), reverse=True)
        recommend_genres = []
        for k,v in sorted_result_dict:
            if v >= 450:
                recommend_genres.append(k)

        pred2 = (select_values * co2) / np.array([np.abs(co2).sum(axis=0)])
        pred_df2 = pd.DataFrame(pred2, index=common_df.index, columns = common_df.columns)
        index = pred_df2.index
        result_dict = {}
        for i in index:
            sorted_tuple = pred_df2.iloc[i].sort_values(ascending=False)
            for genre in sorted_tuple.head(5).index.tolist():
                if genre not in result_dict and genre not in selected_genres:
                    result_dict[genre] = 0
                if genre not in selected_genres:
                    result_dict[genre] += 1
        sorted_result_dict = sorted(result_dict.items(), key=operator.itemgetter(1), reverse=True)
        for k,v in sorted_result_dict:
            if v >= 450 and k not in recommend_genres:
                recommend_genres.append(k)

        # print(recommend_genres)

        first_corr_list = []
        second_corr_list = []
        for g in recommend_genres:
            idx = genre_list.index(g)
            first_corr_value = corr[first_idx][idx]
            first_corr_list.append(first_corr_value)
            second_corr_value = corr[second_idx][idx]
            second_corr_list.append(second_corr_value)

        mean_corr_list = np.array(first_corr_list) + np.array(second_corr_list)
        mean_corr_list = mean_corr_list / 2

        max = mean_corr_list.max()
        mean_list = mean_corr_list.tolist()
        mean_idx = mean_list.index(max)

        result = recommend_genres[mean_idx]
        # print(result)

        temp = selected_genres
        result = list(result.split())
        result = temp+result
        return result