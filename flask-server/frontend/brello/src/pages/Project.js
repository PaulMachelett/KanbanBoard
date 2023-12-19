import { useApiFetch } from "../lib/hooks/useApiFetch";
import { apiRoute } from "../lib/api/api";
import { LinearProgress } from "@mui/material";
import KanbanBoard from "../components/phase/Phase";
import { useContext } from "react";

export const Project = () => {
  // Initialisieren Sie project mit einem leeren Objekt, um auf project.id zuzugreifen, ohne auf undefined zuzugreifen.
  const id = 1;
  const { loading, data: project } = useApiFetch(apiRoute.phases(id));

  console.log("Nach der API-Anfrage, Daten von der API:", project);

  return <>{loading ? <LinearProgress /> : <KanbanBoard phases={project} />}</>;
};
