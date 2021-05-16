from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
import json

client = Client()


# Create your tests here.
class TestAudioFile(TestCase):
    def setUp(self):
        meta_data = {"title": "test",
                     "duration": 40,
                     "uploaded_time": "2022-05-15T00:01:17.951580+05:30",
                     "author": "test_author",
                     "narrator": "test_narrator",
                     "name": "test",
                     "host": "test_host"
                     }

        # dummy instance for song file type
        self.song_audio_file = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "song",
                "meta_data": json.dumps(meta_data)
            },
        )

        # dummy instance for podcast file type
        self.podcast_audio_file = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "podcast",
                "meta_data": json.dumps(meta_data)
            },
        )

        # dummy instance for audiobook file type
        self.audiobook_file = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "audio_book",
                "meta_data": json.dumps(meta_data)
            },
        )
        self.song_id = self.song_audio_file.json()['id']
        self.podcast_id = self.podcast_audio_file.json()['id']
        self.audiobook_id = self.audiobook_file.json()['id']

    # test case to create an object of song type
    # Expected status code: 200
    def test_create_song_audio_file_with_valid_data(self):
        meta_data = {"name": "test",
                     "duration": 40,
                     "uploaded_time": "2022-05-15T00:01:17.951580+05:30"
                     }
        response = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "song",
                "meta_data": json.dumps(meta_data)
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to create an object of podcast type
    # Expected status code: 200
    def test_create_podcast_audio_file_with_valid_data(self):
        meta_data = {"name": "test",
                     "duration": 40,
                     "uploaded_time": "2022-05-15T00:01:17.951580+05:30",
                     "host": "test_host",
                     "participants": ["participant_1"]
                     }
        response = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "podcast",
                "meta_data": json.dumps(meta_data)
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to create an object of audiobook type
    # Expected status code: 200
    def test_create_audiobook_file_with_valid_data(self):
        meta_data = {"title": "test",
                     "duration": 40,
                     "uploaded_time": "2022-05-15T00:01:17.951580+05:30",
                     "author": "test_author",
                     "narrator": "test_narrator"
                     }
        response = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "audio_book",
                "meta_data": json.dumps(meta_data)
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to create podcast with participants more than 10
    # Expected status code: 400
    def test_create_podcast_file_with_participants_greater_than_ten(self):
        meta_data = {"name": "test",
                     "duration": 40,
                     "uploaded_time": "2022-05-15T00:01:17.951580+05:30",
                     "host": "test_host",
                     "participants": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
                     }
        response = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "audio_book",
                "meta_data": json.dumps(meta_data)
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # test case to create podcast object with participants having invalid data type
    # Expected status code: 400
    def test_create_podcast_file_with_invalid_participants(self):
        meta_data = {"name": "test",
                     "duration": 40,
                     "uploaded_time": "2022-05-15T00:01:17.951580+05:30",
                     "host": "test_host",
                     "participants": ""
                     }
        response = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "audio_book",
                "meta_data": json.dumps(meta_data)
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # test case to create podcast object with participants having invalid data type inside the list
    # Expected status code: 400
    def test_create_podcast_file_with_invalid_data_in_participants_list(self):
        meta_data = {"name": "test",
                     "duration": 40,
                     "uploaded_time": "2022-05-15T00:01:17.951580+05:30",
                     "host": "test_host",
                     "participants": [1]
                     }
        response = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "audio_book",
                "meta_data": json.dumps(meta_data)
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # test with past date on any object
    # Expected status code: 400
    def test_create_audio_file_with_invalid_date(self):
        meta_data = {"name": "test",
                     "duration": 40,
                     "uploaded_time": "1998-05-15T00:01:17.951580+05:30"
                     }
        response = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "song",
                "meta_data": json.dumps(meta_data)
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # test case to create podcast object without host
    # Expected status code: 400
    def test_create_audio_file_with_missing_data(self):
        meta_data = {"name": "test",
                     "duration": 40,
                     "uploaded_time": "1998-05-15T00:01:17.951580+05:30"
                     }
        response = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "podcast",
                "meta_data": json.dumps(meta_data)
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # test case to create an object of invalid audio type
    # Expected status code: 400
    def test_create_audio_file_with_invalid_audio_type(self):
        meta_data = {"name": "test",
                     "duration": 40,
                     "uploaded_time": "2022-05-15T00:01:17.951580+05:30"
                     }
        response = client.post(
            reverse('audio_file_create_view',
                    kwargs={}
                    ),
            data={
                "file_type": "invalid_type",
                "meta_data": json.dumps(meta_data)
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # test case to list all objects of song audio type
    # Expected status code: 200
    def test_list_song_audio_type_files(self):
        response = client.get(
            reverse('audio_file_list_view',
                    kwargs={
                        "audio_file_type": "song"
                    }
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to list all objects of podcast audio type
    # Expected status code: 200
    def test_list_podcast_audio_type_files(self):
        response = client.get(
            reverse('audio_file_list_view',
                    kwargs={
                        "audio_file_type": "podcast"
                    }
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to list all objects of audiobook audio type
    # Expected status code: 200
    def test_list_audiobook_audio_type_files(self):
        response = client.get(
            reverse('audio_file_list_view',
                    kwargs={
                        "audio_file_type": "audio_book"
                    }
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to list all objects of some invalid audio type
    # Expected status code: 404
    def test_list_invalid_audio_type_files(self):
        response = client.get(
            reverse('audio_file_list_view',
                    kwargs={
                        "audio_file_type": "invalid_type"
                    }
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to get details of a song object type given its id
    # Expected status code: 200
    def test_get_detail_of_existing_song_object(self):
        response = client.get(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "song",
                        "pk": 1
                    }
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to get details of a podcast object type given its id
    # Expected status code: 200
    def test_get_detail_of_existing_podcast_object(self):
        response = client.get(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "podcast",
                        "pk": 1
                    }
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to get details of an audiobook object type given its id
    # Expected status code: 200
    def test_get_detail_of_existing_audiobook_object(self):
        response = client.get(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "audio_book",
                        "pk": 1
                    }
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to get details of an audiobook object type when given id does not exist
    # Expected status code: 404
    def test_get_detail_of_non_existing_audiobook_object(self):
        response = client.get(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "audio_book",
                        "pk": 2
                    }
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to get details of a podcast object type when given id does not exist
    # Expected status code: 404
    def test_get_detail_of_non_existing_podcast_object(self):
        response = client.get(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "podcast",
                        "pk": 2
                    }
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to get details of a song object type when given id does not exist
    # Expected status code: 404
    def test_get_detail_of_non_existing_song_object(self):
        response = client.get(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "song",
                        "pk": 2
                    }
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to get details of an invalid type
    # Expected status code: 404
    def test_get_detail_of_non_existing_audio_file_type(self):
        response = client.get(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "invalid_type",
                        "pk": 2
                    }
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to update details of a song object type given its id
    # Expected status code: 200
    def test_update_detail_of_existing_song_object(self):
        response = client.patch(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "song",
                        "pk": 1
                    }
                    ),
            data={
                "meta_data": {"name": "updated_name"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to update details of a podcast object type given its id
    # Expected status code: 200
    def test_update_detail_of_existing_podcast_object(self):
        response = client.patch(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "podcast",
                        "pk": 1
                    }
                    ),
            data={
                "meta_data": {"name": "updated_name"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to update details of an audiobook object type given its id
    # Expected status code: 200
    def test_update_detail_of_existing_audiobook_object(self):
        response = client.patch(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "audio_book",
                        "pk": 1
                    }
                    ),
            data={
                "meta_data": {"author": "updated_author"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test case to get details of an audiobook object type when given id does not exist
    # Expected status code: 404
    def test_update_detail_of_non_existing_audiobook_object(self):
        response = client.patch(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "audio_book",
                        "pk": 2
                    }
                    ),
            data={
                "meta_data": {"name": "updated_name"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to update details of a podcast object type when given id does not exist
    # Expected status code: 404
    def test_update_detail_of_non_existing_podcast_object(self):
        response = client.patch(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "podcast",
                        "pk": 2
                    }
                    ),
            data={
                "meta_data": {"name": "updated_name"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to update details of a song object type when given id does not exist
    # Expected status code: 404
    def test_update_detail_of_non_existing_song_object(self):
        response = client.patch(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "song",
                        "pk": 2
                    }
                    ),
            data={
                "meta_data": {"name": "updated_name"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to update details of an invalid type
    # Expected status code: 404
    def test_update_detail_of_non_existing_audio_file_type(self):
        response = client.patch(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "invalid_type",
                        "pk": 2
                    }
                    ),
            data={
                "meta_data": {"name": "updated_name"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to delete song object type given its id
    # Expected status code: 200
    def test_delete_existing_song_object(self):
        response = client.delete(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "song",
                        "pk": 1
                    }
                    ),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # test case to delete a podcast object type given its id
    # Expected status code: 200
    def test_delete_existing_podcast_object(self):
        response = client.delete(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "podcast",
                        "pk": 1
                    }
                    ),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # test case to to delete an audiobook object type given its id
    # Expected status code: 200
    def test_delete_existing_audiobook_object(self):
        response = client.delete(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "audio_book",
                        "pk": 1
                    }
                    ),
            data={
                "meta_data": {"author": "updated_author"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # test case to delete an audiobook object type when given id does not exist
    # Expected status code: 404
    def test_delete_non_existing_audiobook_object(self):
        response = client.delete(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "audio_book",
                        "pk": 2
                    }
                    ),
            data={
                "meta_data": {"name": "updated_name"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to delete a  podcast object type when given id does not exist
    # Expected status code: 404
    def test_delete_non_existing_podcast_object(self):
        response = client.delete(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "podcast",
                        "pk": 2
                    }
                    ),
            data={
                "meta_data": {"name": "updated_name"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to delete a song object type when given id does not exist
    # Expected status code: 404
    def test_delete_non_existing_song_object(self):
        response = client.delete(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "song",
                        "pk": 2
                    }
                    ),
            data={
                "meta_data": {"name": "updated_name"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # test case to delete an invalid type
    # Expected status code: 404
    def test_delete_non_existing_audio_file_type(self):
        response = client.delete(
            reverse('audio_file_update_detail_delete_view',
                    kwargs={
                        "audio_file_type": "invalid_type",
                        "pk": 2
                    }
                    ),
            data={
                "meta_data": {"name": "updated_name"}
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
