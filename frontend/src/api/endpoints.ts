import { httpClient } from "./httpClient";

export const MetricsApi = {
  getOverview: (params?: { zone_id?: string; minutes?: number }) =>
    httpClient.get("/metrics/overview", { params }).then((r) => r.data)
};

export const ZonesApi = {
  list: () => httpClient.get("/zones").then((r) => r.data)
};

export const LogsApi = {
  searchHttp: (payload: {
    dataset: string;
    from?: string | null;
    to?: string | null;
    limit?: number;
  }) => httpClient.post("/logs/search", payload).then((r) => r.data)
};