from tool import Teacher
import requests

class TestTeacher:
    def setup_method(self):
        self.teacher = Teacher('1','1',17)
        self.teacher.logger.info('---start test_login---')
    def test_login(self):
        response = self.teacher.login()
        code = response.json()['code']
        assert code == 2002
        assert response.json()['user']['user_id'] == self.teacher.username
    def test_addClass(self):
        response = self.teacher.addClass()
        assert response.json()['code'] == 2004
        assert response.json()['message'] == '插入class成功'
    def test_deleteClass(self):
        response = self.teacher.deleteClass(96)
        assert response.json()['code'] == 2005
        assert response.json()['message'] == '删除class成功'
    def teardown_method(self):
        self.teacher.logger.info('---end test_login---')
        