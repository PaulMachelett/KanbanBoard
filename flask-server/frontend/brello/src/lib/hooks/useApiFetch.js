import { useEffect, useState } from "react";
/**
 * Hook to fetch Data from the Api
 *
 * @param {*} url apiRoute
 * @param {boolean} polling true = activates short polling effect
 * @returns loading, data, status
 */

export const useApiFetch = (url) => {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);
  const [status, setStatus] = useState(null);

  const fetchApi = () => {
    fetch(url)
      .then((res) => {
        setStatus(res.status);
        if (!res.ok) {
          throw new Error(`${res.status}, ${res.statusText}`);
        }
        return res.json();
      })
      .then((json) => {
        setLoading(false);
        setData(json);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  useEffect(() => {
    fetchApi();
    // eslint-disable-next-line
  }, [url]);

  useEffect(() => {
    /* workaround if token expired -> reload page */
    if (status === 401) window.location.reload();
  }, [status]);

  return { loading, data, status };
};
