import logging
from tool import Teacher
import pytest

class TestTeacher:
    def setup_method(self):
        self.teacher = Teacher('1','1')
        self.teacher.logger.info('---start test_login---')
    def test_login(self):
        self.teacher.login()
    def test_addclass(self):
        self.teacher.addClass()
    def teardown_method(self):
        self.teacher.logger.info('---end test_login---')
        