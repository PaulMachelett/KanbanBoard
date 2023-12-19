import { apiRoute } from "./api";
/**
 *
 * @param {*} data
 */
export const createApiPhase = (data, phaseId) => {
  fetch(apiRoute.createPhase(phaseId), {
    method: "POST",
    headers: {
      Accept: "application/json, text/plain",
      "Content-type": "application/json",
    },
    body: JSON.stringify(data),
  });
};

export const updateApiPhase = (data, phaseId) => {
  fetch(apiRoute.phases(phaseId), {
    method: "PUT",
    headers: {
      Accept: "application/json, text/plain",
      "Content-type": "application/json",
    },
    body: JSON.stringify(data),
  });
};

export const deleteApiPhase = (phase) => {
  fetch(apiRoute.deletePhase(phase), {
    method: "DELETE",
    headers: {
      Accept: "application/json, text/plain",
      "Content-type": "application/json",
    },
  });
};
