require("./node_modules/bootstrap/dist/css/bootstrap.min.css")
import React from 'react';
import ReactDOM from 'react-dom';
let Main = require("./Main.js");

export class App extends React.Component {
	render() {
		return (
			<div>Hello World!</div>
		);
	}
}

ReactDOM.render(<App/>, document.querySelector("#myApp"));
