import 'package:flutter/material.dart'; // materialapp - widgets with diff UI elements
import 'package:flutter/cupertino.dart'; // cupertino icons designed for iOS
import 'package:flutter/foundation.dart'; // framework

void main() { // executes the app
  runApp(
    FriendlyChatApp(), 
  );
}

final ThemeData kIOSTheme = ThemeData( // orange/grey colors if using iOS
  primarySwatch: Colors.purple,
  primaryColor: Colors.grey[100],
  primaryColorBrightness: Brightness.light,
);

final ThemeData kDefaultTheme = ThemeData( // purple/orange colors if using Android 
  primarySwatch: Colors.purple,
  accentColor: Colors.orangeAccent[400],
);

String _name = 'Michelle'; // the username

class FriendlyChatApp extends StatelessWidget {
  const FriendlyChatApp({
    Key key, 
  }) : super(key: key);

  @override
  Widget build(BuildContext context) { // build methods return a widget
    return MaterialApp(
      title: 'FriendlyChat',
      theme: defaultTargetPlatform == TargetPlatform.iOS // cross-platform
          ? kIOSTheme
          : kDefaultTheme,
      home: ChatScreen(), // texting part of screen
    );
  }
}

class ChatMessage extends StatelessWidget {
  ChatMessage({this.text, this.animationController});
  final String text;
  final AnimationController animationController;

  @override
  Widget build(BuildContext context) {
    return SizeTransition(
      sizeFactor:
          CurvedAnimation(parent: animationController, curve: Curves.easeOut),
      axisAlignment: 0.0,
      child: Container(
        margin: EdgeInsets.symmetric(vertical: 10.0),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              margin: const EdgeInsets.only(right: 16.0),
              child: CircleAvatar(child: Text(_name[0])),
            ),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(_name, style: Theme.of(context).textTheme.headline4),
                  Container(
                    margin: EdgeInsets.only(top: 5.0),
                    child: Text(text),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class ChatScreen extends StatefulWidget { // stateful: can be edited
  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> with TickerProviderStateMixin { // state class to hold widgets
  final List<ChatMessage> _messages = [];
  final _textController = TextEditingController(); // widget that provides texting functionality (text field)
  final FocusNode _focusNode = FocusNode(); // widget that allows text field to remain active after sending msg
  bool _isComposing = false; // if there is an unsent message in the input field

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('FriendlyChat'),
        elevation:
            Theme.of(context).platform == TargetPlatform.iOS ? 0.0 : 4.0,
      ),
      body: Container( // positioning of the other widgets within this container
          child: Column(
            children: [
              Flexible( // resize according to screen width
                child: ListView.builder( // list of msgs sent
                  padding: EdgeInsets.all(8.0),
                  reverse: true,
                  itemBuilder: (_, int index) => _messages[index],
                  itemCount: _messages.length,
                ),
              ),
              Divider(height: 1.0), 
              Container(
                decoration: BoxDecoration(color: Theme.of(context).cardColor),
                child: _buildTextComposer(),
              ),
            ],
          ),
          decoration: Theme.of(context).platform == TargetPlatform.iOS 
              ? BoxDecoration(
                  border: Border(
                    top: BorderSide(color: Colors.grey[200]),
                  ),
                )
              : null),
    );
  }

  Widget _buildTextComposer() {
    return IconTheme(
      data: IconThemeData(color: Theme.of(context).accentColor),
      child: Container(
        margin: EdgeInsets.symmetric(horizontal: 8.0),
        child: Row(
          children: [
            Flexible(
              child: TextField(
                controller: _textController,
                onChanged: (String text) {
                  setState(() { // needed to set the state of a state object for different functionalities
                    _isComposing = text.length > 0;
                  });
                },
                onSubmitted: _isComposing ? _handleSubmitted : null, // can't submit empty msgs
                decoration:
                    InputDecoration.collapsed(hintText: 'Send a message'),
                focusNode: _focusNode,
              ),
            ),
            Container(
                margin: EdgeInsets.symmetric(horizontal: 4.0),
                child: Theme.of(context).platform == TargetPlatform.iOS
                    ? CupertinoButton( // grey out send button if text field is empty
                        child: Text('Send'),
                        onPressed: _isComposing
                            ? () => _handleSubmitted(_textController.text)
                            : null,
                      )
                    : IconButton(
                        icon: const Icon(Icons.send),
                        onPressed: _isComposing
                            ? () => _handleSubmitted(_textController.text)
                            : null,
                      ))
          ],
        ),
      ),
    );
  }

  void _handleSubmitted(String text) {
    _textController.clear(); // clear field
    setState(() {
      _isComposing = false;
    });
    ChatMessage message = ChatMessage(
      text: text,
      animationController: AnimationController( // animation when sending text
        duration: const Duration(milliseconds: 700),
        vsync: this,
      ),
    );
    setState(() { // send message
      _messages.insert(0, message);
    });
    _focusNode.requestFocus();
    message.animationController.forward();
  }

  @override
  void dispose() {
    for (ChatMessage message in _messages)
      message.animationController.dispose();
    super.dispose();
  }
}
