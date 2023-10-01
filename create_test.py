import data
import sender_stand_request


def test_getting_order_information():
    track_number = sender_stand_request.post_new_order(data.order_body)
    track = {"t": track_number.json()["track"]}
    response = sender_stand_request.get_orders_trakt(track)
    assert response.status_code == 200


