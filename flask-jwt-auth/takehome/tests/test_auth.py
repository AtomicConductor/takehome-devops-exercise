# takehome/tests/test_auth.py


import time
import json
import unittest

from takehome.tests.base import BaseTestCase


class TestAuthBlueprint(BaseTestCase):

    def test_user_status_expired_token(self):
        """ Test for user status with expired"""
        with self.client:
            response = self.client.get(
                '/v1/user',
                headers=dict(
                    Authorization='Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.\
                        eyJuYmYiOjE1NTQ3NTU1NTUsImV4cCI6MjU1NDc1NTUwMCwiaWF0IjoxNTU0NzU1NT\
                        AwLCJqdGkiOiI5ZmRmMGE2Ni00YzllLTRlOTktODc4MC05YjdlOTNlMjFlMjciLCJ1c2\
                        VyX2lkIjoiMTA1YjM1MTgtNjQ2ZC00NjNlLWFkZGEtZDJiOTM5YzJkMDZkIiwidXNlc\
                        l9mdWxsX25hbWUiOiJCZXJ0cmFtIEdpbGZveWxlIiwidXNlcl9lbWFpbCI6Im51bGxAc\
                        GllZHBpcGVyLmNvbSJ9.-A8Gx18iTikKpedcxDlgcc7D8GMWFix0709Vfpbo1SI'
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Invalid token. Please log in again.')
            self.assertEqual(response.status_code, 401)

    def test_user_status_malformed_bearer_token(self):
        """ Test for user status with malformed bearer token"""
        with self.client:
            response = self.client.get(
                '/v1/user',
                headers=dict(
                    Authorization='xxxxxxxx'
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Bearer token malformed.')
            self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
