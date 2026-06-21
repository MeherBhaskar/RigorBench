import os

def test_main():
    app_js_path = os.path.join(os.path.dirname(__file__), 'App.js')
    with open(app_js_path, 'r') as f:
        content = f.read()

    assert 'react-router-dom' in content, "react-router-dom is not imported"
    assert 'BrowserRouter' in content or 'Router' in content, "Router is not used"
    assert 'Routes' in content or 'Switch' in content, "Routes is not used"
    assert 'Route' in content, "Route is not used"
    assert '<Route path="/"' in content or "<Route path='/'" in content or "path=\"/\"" in content, "Home route is not defined"
    assert 'path="/about"' in content or "path='/about'" in content, "About route is not defined"

if __name__ == '__main__':
    test_main()
    print('All tests passed!')
