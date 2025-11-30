import React from "react";

type Props = {
  title: string;
  value: string | number;
  subtitle?: string;
};

export const KpiCard: React.FC<Props> = ({ title, value, subtitle }) => {
  return (
    <div
      style={{
        padding: "12px 16px",
        borderRadius: 8,
        border: "1px solid #ddd",
        background: "#fff",
        boxShadow: "0 1px 3px rgba(0,0,0,0.05)",
        display: "flex",
        flexDirection: "column",
        gap: 4
      }}
    >
      <div style={{ fontSize: 12, color: "#666" }}>{title}</div>
      <div style={{ fontSize: 22, fontWeight: 600 }}>{value}</div>
      {subtitle && (
        <div style={{ fontSize: 12, color: "#999" }}>{subtitle}</div>
      )}
    </div>
  );
};