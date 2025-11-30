import React from "react";

export type LogRow = {
  timestamp: string;
  zone_name?: string;
  http_host?: string;
  http_path?: string;
  http_status?: number;
  firewall_action?: string | null;
  client_country?: string | null;
  client_ip?: string | null;
};

type Props = {
  rows: LogRow[];
};

export const LogsTable: React.FC<Props> = ({ rows }) => {
  return (
    <div style={{ overflowX: "auto" }}>
      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          fontSize: 12
        }}
      >
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Zone</th>
            <th>Host</th>
            <th>Path</th>
            <th>Status</th>
            <th>Action</th>
            <th>Country</th>
            <th>IP</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r, idx) => (
            <tr key={idx}>
              <td>{r.timestamp}</td>
              <td>{r.zone_name}</td>
              <td>{r.http_host}</td>
              <td>{r.http_path}</td>
              <td>{r.http_status}</td>
              <td>{r.firewall_action}</td>
              <td>{r.client_country}</td>
              <td>{r.client_ip}</td>
            </tr>
          ))}
          {rows.length === 0 && (
            <tr>
              <td colSpan={8} style={{ textAlign: "center", padding: 16 }}>
                Nenhum log disponível.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};