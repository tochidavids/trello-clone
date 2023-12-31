import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./styles/styles.css";

export const getDatabaseData = async model => {
	const res = await fetch(`http://127.0.0.1:8000/api/${model}`);
	const data = await res.json();
	console.log(model, "data:", data);
	return data;
};
getDatabaseData("current-user");

export const createWorkspace = async formInfo => {
	fetch("/api/workspaces", {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: {
			name: formInfo.name,
			description: formInfo.description,
			creator: formInfo.user,
			members: formInfo.members,
		},
	});
};

export const logout = async event => {
	event.preventDefault();
	fetch("/logout", {
		method: "post",
		headers: { "Content-Type": "application/json" },
		// body: {},
	});
};

ReactDOM.createRoot(document.getElementById("root")).render(
	<React.StrictMode>
		<App />
	</React.StrictMode>,
);
