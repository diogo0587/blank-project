import React from "react";
import { BrowserRouter, Routes, Route, Navigate, Link } from "react-router-dom";
import { OverviewPage } from "../pages/OverviewPage";
import { LiveLogsPage } from "../pages/LiveLogsPage";

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <div style={{ display: "flex", minHeight: "100vh", fontFamily: "system-ui, sans-serif" }}>
      <aside
        style={{
          width: 220,
          background: "#111827",
          color: "#e5e7eb",
          padding: "16px 12px",
          display: "flex",
          flexDirection: "column",
          gap: 8
        }}
      >
        <div style={{ fontWeight: 600, marginBottom: 12 }}>CF Ops &amp; Observability</div>
        <nav style={{ display: "flex", flexDirection: "column", gap: 4 }}>
          <Link style={{ color: "#e5e7eb", textDecoration: "none" }} to="/overview">
            Visão geral
          </Link>
          <Link style={{ color: "#e5e7eb", textDecoration: "none" }} to="/logs/live">
            Logs ao vivo
          </Link>
        </nav>
      </aside>
      <main style={{ flex: 1, background: "#f3f4f6" }}>{children}</main>
    </div>
  );
};

export const AppRouter: React.FC = () => (
  <BrowserRouter>
    <Layout>
      <Routes>
        <Route path="/" element={<Navigate to="/overview" replace />} />
        <Route path="/overview" element={<OverviewPage />} />
        <Route path="/logs/live" element={<LiveLogsPage />} />
      </Routes>
    </Layout>
  </BrowserRouter>
);