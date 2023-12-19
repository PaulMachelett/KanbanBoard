import * as React from "react";
import { Component } from "react";
import { Link } from '@material-ui/core';

/**
 *@fileOverview Zeigt alle Mitwirkenden im Projekt mit Verweis auf die Git-Repository
 *@author Melisa Yilmaz
*/

export class About extends Component {

  render() {
    return (
      <div>
        <h2>
          Software-Praktikum im WS 2023/24
        </h2>
        <br />
        <p>
          React Frontend written by
          <Link href='https://github.com/MelisaYilmaz01'> Melisa Yilmaz, </Link>
          <Link href='https://github.com/TomBeier99'>Tom Beier, </Link>
          <Link href='https://github.com/tomknittel'>Tom Knittel, </Link>
          <Link href='https://github.com/fmaierfm091'>Fabrice Maier</Link>
        </p>
        <p>
          Python Backend written by
          <Link href='https://github.com/PaulMachelett'> Paul Machelett, </Link>
          <Link href='https://github.com/AlexCasapu'>Alex Casapu </Link>
        </p>
        <br />
        <p variant='body2'>
          © Gruppe 6 2023/24, all rights reserved.
        </p>
      </div>
    )
  }

};
export default About;

