__author__ = 'yangweidong'
from controller.system.showmqttdatacontrolletr import ShowMqttDataView,NewMqttDtaView

def route(app):
    app.add_url_rule('/', view_func=ShowMqttDataView.as_view('ShowMqttDataView'), methods=['Post', 'GET'])
    app.add_url_rule('/new', view_func=NewMqttDtaView.as_view('NewMqttDtaView'), methods=['Post', 'GET'])