from frame.app import create_app

app = create_app()

import module

module.init_app(app)

if __name__ == '__main__':
    # 启动web服务
    app.run('0.0.0.0', port=app.config.get("RUN_PORT"), debug=True)
