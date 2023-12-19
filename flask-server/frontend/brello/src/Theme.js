import { createTheme } from '@mui/material/styles'
import { colors } from '@mui/material';

/**A custom theme for the app */
const Theme = createTheme({
    palette: {
      primary: {
        mode: 'dark',
        
        light: '#757ce8',
        main: '#3f50b5',
        dark: '#002884',
        contrastText: '#fff',
      },
      secondary: {
        light: '#ff7961',
        main: '#f44336',
        dark: '#ba000d',
        contrastText: '#000',
      },
      error: {
        main: colors.red[400],
      },
      background: {
        paper: '#ffffff',
        default: '#fff',
      },
    },
  });
  
  
  export default Theme;