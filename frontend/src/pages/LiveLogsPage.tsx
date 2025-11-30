import React, { useEffect, useState } from "react";
import { LogsApi } from "../api/endpoints";
import { LogsTable, LogRow } from "../components/tables/LogsTable";

export const LiveLogsPage: React.FC = () => {
  const [rows, setRows] = useState<LogRow[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchLogs = () => {
      LogsApi.searchHttp({
        dataset: "http",
        from: null,
        to: null,
        limit: 200
      })
        .then((data) => {
          // Assumindo que o backend retorna uma lista de eventos já normalizados
          setRows(data);
          setError(null);
        })
        .catch((err) => {
          console.error("Erro ao buscar logs", err);
          setError("Falha ao carregar logs.");
        });
    };

    fetchLogs();
    const id = setInterval(fetchLogs, 5000);
    return () => clearInterval(id);
  }, []);

  return (
    <div style={{ padding: 24 }}>
      <h1>Logs ao vivo</h1>
      {error && <div style={{ color: "red" }}>{error}</div>}
      <LogsTable rows={rows} />
    </div>
  );
};