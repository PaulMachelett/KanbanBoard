import { useApiFetch } from "../lib/hooks/useApiFetch";
import { apiRoute } from "../lib/api/api";
import { LinearProgress } from "@mui/material";
import Projectview from "../components/project/Project.js";

export const Home = () => {
  const id = 3;
  const { loading, data: home } = useApiFetch(apiRoute.project(id));
  
  console.log("Nach der API-Anfrage, Daten von der API:", home);

  return <>{loading ? <LinearProgress /> : <Projectview project={home} />}</>;
};
