const baseURL = "";

export const apiRoute = {
  users: `${baseURL}/users`,
  user: (id) => `${baseURL}/users/${id}`,
  userByName: (name) => `${baseURL}/users/search/${name}`,
  userByGoogleId: (g_id) => `${baseURL}/users/google/${g_id}`,
  profile: (userId) => `${baseURL}/profiles/${userId}`,
  project: (projectid) => `${baseURL}/projectparticipation/projects/${projectid}`,
  phases: (projectid) => `${baseURL}/phase/project/${projectid}`,
  createPhase:() => `${baseURL}/phase`,
  deletePhase:(phaseId) => `${baseURL}/phase/${phaseId}`, 
};
