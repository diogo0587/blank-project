import React, { useEffect, useState } from "react";
import { MetricsApi } from "../api/endpoints";
import { KpiCard } from "../components/cards/KpiCard";

export const OverviewPage: React.FC = () => {
  const [metrics, setMetrics] = useState<any | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    MetricsApi.getOverview({ minutes: 60 })
      .then((data) => {
        setMetrics(data);
        setError(null);
      })
      .catch((err) => {
        console.error("Failed to load metrics", err);
        setError("Falha ao carregar métricas.");
      });
  }, []);

  return (
    <div style={{ padding: 24 }}>
      <h1>Visão Geral</h1>
      {error && <div style={{ color: "red" }}>{error}</div>}
      {!metrics && !error && <div>Carregando...</div>}
      {metrics && (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))",
            gap: 16,
            marginTop: 16
          }}
        >
          <KpiCard
            title="Reqs (janela)"
            value={metrics.total_requests}
            subtitle={`${metrics.window_minutes} minutos`}
          />
          <KpiCard title="Erros 4xx" value={metrics.errors_4xx} />
          <KpiCard title="Erros 5xx" value={metrics.errors_5xx} />
          <KpiCard
            title="Taxa 4xx"
            value={(metrics.error_4xx_rate * 100).toFixed(2) + "%"}
          />
          <KpiCard
            title="Taxa 5xx"
            value={(metrics.error_5xx_rate * 100).toFixed(2) + "%"}
          />
        </div>
      )}
    </div>
  );
};