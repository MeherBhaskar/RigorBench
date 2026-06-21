import pytest
from main import process_data_stream

def test_process_data_stream_all_valid():
    stream = ['{"a": 1}', '{"b": 2}']
    valid, errors = process_data_stream(stream)
    assert valid == [{"a": 1}, {"b": 2}]
    assert errors == []

def test_process_data_stream_with_invalid():
    stream = ['{"a": 1}', 'invalid_json', '{"b": 2}', '{missing_quotes: 3}']
    valid, errors = process_data_stream(stream)
    assert valid == [{"a": 1}, {"b": 2}]
    assert errors == ['invalid_json', '{missing_quotes: 3}']

def test_process_data_stream_all_invalid():
    stream = ['invalid1', 'invalid2']
    valid, errors = process_data_stream(stream)
    assert valid == []
    assert errors == ['invalid1', 'invalid2']
