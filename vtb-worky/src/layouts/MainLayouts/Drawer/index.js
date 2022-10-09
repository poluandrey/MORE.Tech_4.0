import { Box, useMediaQuery, Drawer } from "@mui/material"
import { useTheme } from '@mui/material/styles';
import { useMemo } from "react";
import PropTypes from 'prop-types'

import drawerWidth from '../../../conf'

import DrawerContent from "./DrawerContent";
import DrawerHeader from "./DrawerHeader";
import MiniDrawerStyled from "./MiniDrawerStyled";

const MainDrawer = ({ open, handleDrawerToggle, window }) => {
    const theme = useTheme()
    const matchDownMD = useMediaQuery(theme.breakpoints.down('lg'));

    const container = window !== undefined ? () => window().document.body : undefined;

    const drawerContent = useMemo(() => <DrawerContent />, []);
    const drawerHeader = useMemo(() => <DrawerHeader open={open} />, [open]);

    return (
        <Box component="nav" sx={{ flexShrink: { md: 0 }, zIndex: 1300 }} aria-label="mailbox folders">
        {!matchDownMD ? (
            <MiniDrawerStyled variant="permanent" open={open}>
                {drawerHeader}
                {drawerContent}
            </MiniDrawerStyled>
        ) : (
            <Drawer
                container={container}
                variant="temporary"
                open={open}
                onClose={handleDrawerToggle}
                ModalProps={{ keepMounted: true }}
                sx={{
                    display: { xs: 'block', lg: 'none' },
                    '& .MuiDrawer-paper': {
                        boxSizing: 'border-box',
                        width: drawerWidth,
                        borderRight: `1px solid ${theme.palette.divider}`,
                        backgroundImage: 'none',
                        boxShadow: 'inherit'
                    }
                }}
            >
                {drawerHeader}
                {open && drawerContent}
            </Drawer>
        )}
        </Box>
    )
}

MainDrawer.propTypes = {
    open: PropTypes.bool,
    handleDrawerToggle: PropTypes.func,
    window: PropTypes.object
};

export default MainDrawer;