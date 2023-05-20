var socketio;
$(document).ready(function(){
socketio = io.connect('http://' + document.domain + ':' + location.port + '/chat');

socketio.on('connect', function() {
    socketio.emit('joined', {});
});

socketio.on('status', function(data) {
    $('#chat').val($('#chat').val() + '<' + data.msg + '>\n');
    $('#chat').scrollTop($('#chat')[0].scrollHeight);
});

socketio.on('message', function(data) {
    $('#chat').val($('#chat').val() + data.msg + '\n');
    $('#chat').scrollTop($('#chat')[0].scrollHeight);
});

$('#text').keypress(function(e) {
    var code = e.keyCode || e.which;
    if (code == 13) {
        text = $('#text').val();
        socketio.emit("text", {msg: text});
        $('#text').val('');
    }
});
});
function leave_room() {
    socketio.emit('leave', {}, function() {
        socketio.disconnect();
        window.loaction.href = "{{ url_for('home') }}";
    });
}

/*
const messages = document.getElementById("messages");
const createMessage = (message) => {
    const content = `
        <div class="text">
            <span>
                <strong>${message}</strong>
            </span>
            <span class="muted">
                ${new date().toLocaleString()}
                <!-- Need to change the above -->
            </span>
        </div>
    `;
    messages.innerHTML += content;
};

socketio.on("message"), (data) => {
    createMessage(data.msg);
    console.log("received msg from server");
};

const sendMessage = () => {
    const message = document.getElementById("message");
    if (message.value == "") return;
    socketio.emit("text", {data: message.value});
    message.value = "";
};
*/