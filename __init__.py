from luci_auto import LucidityAuto as LA

class LucidityAuto:
    """
    What is LucidityAuto:
    Hi, I'm a Parser for easy to publish (Use functions from a module named 'Lucidity')
    Save own pattern of path that the studio have from project file.
    Input 'nickname' of pattern and 'path' from your sequence. Now easy parsing with LucidityAuto!

    LucidityAuto란?
    아티스트가 작업 종료 후, 해당 작업물을 퍼블리시하기 위해 사용하는 툴.
    스튜디오에 저장한 모든 파일의 경로를 사전에 합의한 패턴 값으로 지정하고 추출할 수 있는 파싱 프로그램.
    'Lucidity'의 기능을 이용한 자동화 버전이다.
    """

"""
< How to use 'LucidityAuto' >

    1. print(LA.template_key)를 사용하여 저장되어 있는 템플릿 목록을 확인합니다.

    2. 1번의 목록 중 사용할 템플릿의 이름을 LA.template_name에 작성해주세요.
     
    2-2. 필요한 템플릿이 없다면 LA.add_template 기능을 활용하여 새 템플릿을 추가합니다.

    ex. LA.add_template('템플릿의 이름', '템플릿화 하고 싶은 패턴 정보')
        LA.add_template('houdini', '/home/rapa/project/{project}/shot/{seq}/{shot}/'
                                    '{dept}/{ver}/{seq}_{shot}_{dept}_{ver}.{ext}')

    3. 2번에서 템플릿을 선택한 후, 작업을 끝낸 파일의 절대경로를 data칸에 함께 입력해 주세요.
    ex. data = LA.set_path('/home/rapa/project/avata/shot/boo/0010/plate/v001/boo_0010_plate_v001.0010.jpg')
    
    3-2. print(data)를 이용하시면 자동으로 parsing된 값을 확인할 수 있습니다!

    4. 원하는 정보 하나만 얻고 싶다면 아래와 같이 활용하세요. :)
    ex)print(data["project"]),
       print(data["seq"]),
       print(data["shot"]),
       print(data["dept"]),
       print(data["ver"]),
       print(data["padding"]),
       print(data["ext"])
"""
