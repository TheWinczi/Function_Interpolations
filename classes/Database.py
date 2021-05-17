import pandas
from typing import List


class Database(object):
    """ Class representing Database in project 3.
        Object storing height profiles using in
        other functions """

    def __init__(self):
        """ Initialize the object """
        self.__data = {}

    def add_data(self, new_data_name: str, new_data):
        """ add new data to database
            @:param new_data_name - name of the new data database
            @:param new_data - new data to database """

        if new_data_name in self.__data.keys():
            print('Key {0} is already existed in database'.format(new_data_name))
        else:
            self.__data[new_data_name] = new_data

    def get_data(self, data_name: str):
        """ get data in defined name
            @:param data_name - name of the data to get """

        if data_name in self.__data.keys():
            return self.__data[data_name]
        else:
            print('There is not any keys named {0} in database'.format(data_name))
            return None

    def clear(self):
        """ clear all data in database """
        for key in self.__data.keys():
            del self.__data[key]

    def load_all_data(self, data_names_list: List[str], data_paths_list: List[str]):
        """ load all data
            @:param data_names_list - list of data names
            @:param data_paths_list - list of paths to data .csv """

        for i, name in enumerate(data_names_list):
            try:
                self.__data[name] = pandas.read_csv(data_paths_list[i])
            except IOError:
                pass

        print('All data have loaded')

    def get_column_by_name(self, data_name: str, column_name: str, as_list: bool = True):
        """ get column with specific name """
        data = self.__data[data_name][column_name]
        if as_list:
            return list(data)
        else:
            return data

    def get_data_names(self):
        """ get all data names in database names as list """
        return list(self.__data.keys())

    def get_all_data(self, copy: bool = True):
        """ get all data from database """
        if copy:
            return self.__data.copy()
        else:
            return self.__data
