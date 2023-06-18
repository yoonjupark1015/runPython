import lucidity
import os
import json


class LucidityAuto:
    """
    What is LucidityAuto:
    Hi, I'm a Parser for easy to publish (Use functions from a module named 'Lucidity')
    Save own pattern of path that the studio have from project file.
    Input 'nickname' of pattern and 'path' from your sequence. Now easy parsing with LucidityAuto!
    """

    def __init__(self):
        """
        Initialization.

        templates: set in 'dictionary' form to add patterns
        template: set in 'Lucidity' form to save a pattern
        set_path: input 'file_path' and get parse data automatically
        template_name: key of value, title of pattern
        json_path: path of json file that saved templates
        load_template: open and load 'self._templates' in json file
        """
        self._templates = {}
        self._template = None
        self._set_path = ""
        self._template_name = ""
        self._json_path = "./myluci.json"
        self.load_template()

    @property
    def templates(self):
        """
        read only
        Returns:
            dict: every template in .json
        """
        return self._templates

    @templates.setter
    def templates(self, value):
        """
        A collection of all templates. (cf. add_template() )
        Args:
            value (str): template(nickname and pattern) from add_template()
        """
        self._templates = value

    @property
    def template(self):
        """
        read only
        Returns:
            str: template
        """
        return self._template

    @template.setter
    def template(self, value):
        """
        make template from nickname(key) and pattern(value) information entering the dictionary(json file)
        Args:
            value (str): It receives two factor values.
        """
        self._template = value

    @property
    def template_name(self):
        """
        read only
        Returns:
            str: template_name
        """
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        """
        if enter the template_name, can set template automatically
        Args:
            value (str): template_name. The title of pattern, 'nickname'
        """
        self._template_name = value
        if value not in self._templates:
            raise ValueError("Error: Please enter only the template name that exists in the list."
                             "리스트에 존재하는 템플릿 이름만 입력해 주세요.")
        self._set_template()

    def add_template(self, nickname, pattern):
        """
        save as json file after add new template with nickname and pattern
        Args:
            nickname (str): name of pattern, key of value
            pattern (str): pattern of path for parsing, value of key
        """
        self.templates[nickname] = pattern
        self.save_template()

    def save_template(self):
        """
        save as json file to json_path (cf. __init__())
        """
        with open(self._json_path, "w") as json_file:
            json.dump(self.templates, json_file)

    def load_template(self):
        """
        load json file (cf. json_path)
        """
        if os.path.exists(self._json_path):
            with open(self._json_path, "r") as json_file:
                self.templates = json.load(json_file)

    @property
    def template_key(self):
        """
        get every nickname of patterns in templates
        Returns:
            list: every template list in json
        """
        return list(self.templates.keys())

    def _set_template(self):
        """
        set template automatically when you input template_name in list ( cf. template_name() )
        """
        nickname = self.template_name
        pattern = self.templates[nickname]
        self.template = lucidity.Template(nickname, pattern)

    def set_path(self, path):
        """
        get parsing data from file path with template in json(kind of dictionary)
        Args:
            path (str): file path(Absolute Path) in directory

        Returns:
            dict: parse path with pattern in json
        """
        data = self.template.parse(path)
        return data


def main():
    LA = LucidityAuto()
    # e.g. LA.add_template('houdini', '/home/rapa/project/{project}/shot/{seq}/{shot}/'
    #                                '{dept}/{ver}/{seq}_{shot}_{dept}_{ver}.{ext}')
    # get template list as title(key)
    print(LA.template_key)
    # use case
    LA.template_name = "houdini"
    data = LA.set_path('/home/rapa/project/topgun/shot/boo/0010/'
                       'plate/v001/boo_0010_plate_v001.0001.jpg')
    print(data)
    print(data["project"])
    os.getcwd()


if __name__ == '__main__':
    main()