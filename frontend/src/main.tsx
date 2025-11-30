import React from "react";
import ReactDOM from "react-dom/client";
import { AppRouter } from "./router";

const rootElement = document.getElementById("root");

if (rootElement) {
  ReactDOM.createRoot(rootElement).render(
    <React.StrictMode>
      <AppRouter />
    </React.StrictMode>
  );
}