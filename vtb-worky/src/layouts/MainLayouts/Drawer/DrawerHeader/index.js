import PropTypes from 'prop-types';
import { useTheme } from '@mui/material/styles';
import DrawerHeaderStyled from './DrawerHeaderStyled';
import { Typography } from '@mui/material';

const DrawerHeader = ({ open }) => {
  const theme = useTheme();

  return (
    <DrawerHeaderStyled theme={theme} open={open}>
        {open ? <Typography variant='h3' color='#0A2896'>VTB.WORKY</Typography>
        : <Typography variant='h3' color='#0A2896'>VTB</Typography>}
    </DrawerHeaderStyled>
  );
};

DrawerHeader.propTypes = {
  open: PropTypes.bool
};

export default DrawerHeader;
