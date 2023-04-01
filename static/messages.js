function Messages(props) {
    const [messages, setMessages] = React.useState([]);
    const [num, setNum] = React.useState([]);
    const getMessages = () => {
        axios.get("/messages").then((result) => {
            setMessages(result.data);
        })
        axios.get("/num").then((result) => {
            setNum(result.data);
        })
    }
    React.useEffect(() => {
        getMessages();
        setInterval(getMessages, props.interval);
    }, []
    )
    return (
        <div>
            <h3>Messages</h3>
            <div>{messages.map((item) =>
                <div>{item}</div>
            )}</div>
            <button onClick={getMessages}>Get New Messages</button>
            <div>
                You have {num} messages
            </div>
        </div>
    );
}

ReactDOM.render(<Messages interval={60 * 60 * 1000} />, document.getElementById("messages"));
