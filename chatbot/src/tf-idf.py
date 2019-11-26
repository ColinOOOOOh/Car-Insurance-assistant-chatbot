## Import Libraries and Modules here...
import spacy
import pickle
from collections import Counter
from math import log
from itertools import combinations
from collections import Counter
from spacy.kb import KnowledgeBase
from spacy.vocab import Vocab
from spacy.pipeline import EntityLinker


class InvertedIndex:
    def __init__(self):
        ## You should use these variable to store the term frequencies for tokens and entities...
        self.tf_tokens = None
        self.tf_entities = None

        ## You should use these variable to store the inverse document frequencies for tokens and entities...
        self.idf_tokens = None
        self.idf_entities = None

## Your implementation for indexing the documents...

    def index_documents(self, documents):
        entities_list = []
        token_list = []
        entities_dic = {}
        tokens_dic = {}
        index_entities = {}
        index_tokens = {}
        new_token_dict = {}
        new_entity_dict = {}
        idf_token_norm = {}
        idf_entities_norm = {}
        tf_tokens_norm = {}
        tf_entities_norm = {}
        nlp = spacy.load("en_core_web_sm")
        kb = KnowledgeBase(vocab=nlp.vocab, entity_vector_length=3)
        entity_linker = EntityLinker(nlp.vocab)
        entity_linker.set_kb(kb)
        #kb = KnowledgeBase(vocab=nlp.vocab, entity_vector_length=3)
        kb.add_entity(entity="glass insurance", freq=6, entity_vector=[0, 3, 5])
        kb.add_entity(entity="robber insurance", freq=342, entity_vector=[1, 9, -3])
        a= kb.get_entity_strings()
        #entity_linker = EntityLinker(nlp.vocab)
        #entity_linker.set_kb(kb)
        #print(a)
        tol_number_doc = len(documents)
        #print(tol_number_doc)
        for doc_id, value in documents.items():
            doc = nlp(value)
            entities_list = []
            token_list = []
            entities_dic = {}
            tokens_dic = {}
            counter_document = {}
            counter_entity = {}
            #print(doc)
            for ent in doc.ents:
                entities_list.append(ent.text)
            #print(entities_list)
            for ent in doc.ents:
                counter_entity[ent.text] = entities_list.count(ent.text)

                entities_dic[ent.text] = {
                    doc_id: entities_list.count(ent.text)
                }
            #print(counter_entity)
            index_entities[doc_id] = entities_dic
            #print(index_entities)

            for token in doc:
                if token.is_stop == False and token.is_punct == False:
                    token_list.append(token.text)

            for token in doc:
                if token.is_stop == False and token.is_punct == False:
                    counter_document[token.text] = token_list.count(token.text)
                    
            for ent in entities_list:
                ent = ent.split(' ')
                if len(ent) == 1:
                    if ent[0] in counter_document.keys():
                        if counter_document[ent[0]] - counter_entity[
                                ent[0]] >= 1:
                            counter_document[ent[0]] = counter_document[
                                ent[0]] - 1
                        else:
                            del counter_document[ent[0]]
            # print(counter_document)

            for token in doc:
                if token.is_stop == False and token.is_punct == False:
                    if token.text in counter_document.keys():
                        tokens_dic[token.text] = {
                            doc_id: counter_document[token.text]
                        }
            #print(counter_document)
            index_tokens[doc_id] = tokens_dic
            print(index_tokens)

        for doc_id in index_entities.keys():
            for key1 in index_entities[doc_id].keys():
                if key1 not in new_entity_dict.keys():
                    new_entity_dict[key1] = {}
                for key2 in index_entities[doc_id][key1].keys():
                    new_entity_dict[key1][key2] = index_entities[doc_id][key1][
                        key2]
        #print(new_entity_dict)
        for doc_id in index_tokens.keys():
            for key1 in index_tokens[doc_id].keys():
                if key1 not in new_token_dict.keys():
                    new_token_dict[key1] = {}
                for key2 in index_tokens[doc_id][key1].keys():
                    new_token_dict[key1][key2] = index_tokens[doc_id][key1][
                        key2]
        #print(new_token_dict)
        for ent, counter in new_entity_dict.items():
            #print(counter.values())
            for j in counter.keys():
                counter[j] = 1 + log(counter[j])
            #print(counter)
            tf_entities_norm[ent] = counter
        print(tf_entities_norm)
        for token, counter in new_token_dict.items():
            #print(counter.values())
            for j in counter.keys():
                counter[j] = 1 + log(1 + log(counter[j]))
            #print(counter)
            tf_tokens_norm[token] = counter

        #print(tf_tokens_norm)
        for ent, counter in new_entity_dict.items():
            tol_ctain_ent = len(counter)
            idf_entities_norm[ent] = 1.0 + log(tol_number_doc /
                                               (1.0 + tol_ctain_ent))
        #print(idf_entities_norm)

        for token, counter in new_token_dict.items():
            tol_ctain_token = len(counter)
            idf_token_norm[token] = 1.0 + log(tol_number_doc /
                                              (1.0 + tol_ctain_token))
        #print(idf_token_norm)

        # print(tf_tokens_norm)
        # print(tf_entities_norm)
        self.tf_tokens = tf_tokens_norm
        self.tf_entities = tf_entities_norm
        self.idf_tokens = idf_token_norm
        self.idf_entities = idf_entities_norm


## Your implementation to split the query to tokens and entities...

    def split_query(self, Q, DoE):
        split_list = []
        split_query = []
        legal_entity = []
        new_list = []
        new_str = ''
        dic_count_token = {}
        new_str_list = []
        com_dic = {}
        com_e_t_list = []
        for ent in DoE.keys():
            split_list.append(ent)
        #print(split_list)
        for i in range(1, len(split_list) + 1):
            a = list((combinations(split_list, i)))
            #print(a)
            for j in a:
                split_query.append(list(j))
        #print(split_query)
        Q_list = Q.split(' ')
        #print(Q_list)
        count_query_dic = dict(Counter(Q_list))
        #print(count_query_dic)

        for item in split_query:
            jug_nub = 0
            new_str = ''
            #print(item)
            dic_count_token = {}
            for i in range(0, len(item)):
                new_str = new_str + ' ' + item[i]
            #print(new_str)
            new_str_list = new_str.split(' ')
            #print(new_str_list)
            update_list = new_str_list[1:]
            #print(update_list)
            for i in update_list:
                dic_count_token[i] = update_list.count(i)
            #print(dic_count_token)
            for i in dic_count_token:
                if i not in count_query_dic.keys(
                ) or dic_count_token[i] > count_query_dic[i]:
                    jug_nub = 1
            if jug_nub == 0:
                legal_entity.append(item)
        #print(legal_entity)
        com_dic['tokens'] = Q_list
        com_dic['entities'] = []
        com_e_t_list.append(com_dic)
        #print(com_e_t_list)
        for new_item in legal_entity:
            new_list = []
            com_dic = {}
            up_str = ''
            for i in range(0, len(new_item)):
                up_str = up_str + ' ' + new_item[i]
            #print(up_str)
            up_str_list = up_str.split(' ')
            com_list = up_str_list[1:]
            #print(com_list)
            copy_list = Q_list.copy()
            for i in Q_list:
                if i not in com_list or copy_list.count(i) > com_list.count(i):
                    new_list.append(i)
                    if i in com_list:
                        copy_list.remove(i)

            #print(new_list)
            com_dic['tokens'] = new_list
            com_dic['entities'] = new_item
            com_e_t_list.append(com_dic)
        #print(com_e_t_list)
        return com_e_t_list
        #print(com_e_t_list)

        ## Your implementation to return the max score among all the query splits...
    def max_score_query(self, query_splits, doc_id):
        result_list = []
        final_result_list = []
        for i in query_splits:
            #print(i)
            s2 = 0
            s1 = 0
            com_score = 0
            for j in i['tokens']:
                if j == []:
                    s2 = 0.0
                if j not in self.tf_tokens.keys():
                    s2 += 0.0

                if j in self.tf_tokens.keys(
                ) and doc_id in self.tf_tokens[j].keys():
                    s2 = s2 + self.tf_tokens[j][doc_id] * self.idf_tokens[j]
            #print(s2)
            for k in i['entities']:
                if k == []:
                    s1 = 0.0
                if j not in self.tf_entities.keys():
                    s1 += 0.0
                if k in self.tf_entities.keys(
                ) and doc_id in self.tf_entities[k].keys():
                    s1 = s1 + self.tf_entities[k][doc_id] * self.idf_entities[k]
            #print(s1)
            com_score = s1 + s2 * 0.4
            final_score = s1
            #print(com_score)
            #result_tuple = (com_score, i)
            result_tuple = (final_score,i)
            #print(final_score)

            #print(result_tuple)
            result_list.append(result_tuple)
        #print(result_list)
        final_result_list = sorted(result_list,
                                   key=lambda result_list: result_list[0])
        #print(final_result_list)
        final_result = final_result_list[-1]
        #print(final_result)
        return final_result

