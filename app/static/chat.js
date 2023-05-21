// FUNCTIONALITY - written by @yelnats8
var socketio;
$(document).ready(function(){
socketio = io.connect('http://' + document.domain + ':' + location.port + '/chat');

socketio.on('connect', function() {
    socketio.emit('joined', {});
});

socketio.on('status', function(data) {
    statusMessage(data);
    $('#chat').val($('#chat').val() + '<' + data.msg + '>\n');
    $('#chat').scrollTop($('#chat')[0].scrollHeight);
});

socketio.on('message', function(data) {
    createMessage(data);
    console.log("received msg from server");
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

const messages = document.getElementById("messages");
const createMessage = (data) => {
    var link = "/user/" + encodeURIComponent(data.user);
    const content = `
        <div class="text">
            <span>
                <a href=${link}><strong>${data.user}:</strong></a>
                 ${data.msg}
            </span>
            <span class="muted">
                <!-- Need to change the above -->
            </span>
        </div>
    `;
    messages.innerHTML += content;
};

const statusMessage = (data) => {
    var link = "/user/" + encodeURIComponent(data.user);
    const content = `
        <div class="text">
            <span>
                <a href=${link}><strong>${data.user}</strong></a>
                 <strong>${data.msg}</strong>
            </span>
            <span class="muted">
                <!-- Need to change the above -->
            </span>
        </div>
    `;
    messages.innerHTML += content;
};

const sendMessage = () => {
    const message = document.getElementById("message");
    if (message.value == "") return;
    socketio.emit("text", {msg: message.value});
    message.value = "";
};


// DISPLAY
var messageDiv = document.getElementsByClassName("messageDiv")[0];
var messageField = document.getElementsByClassName("messageField")[0];

messageDiv.addEventListener('click', function() {
    messageField.focus();
});