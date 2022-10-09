import Search from "./Search";
import { useMediaQuery } from "@mui/material";

const HeaderContent = () => {

    const matchesXs = useMediaQuery((theme) => theme.breakpoints.down('md'));

    return (
        <>
            { !matchesXs && <Search /> }
        </>
    )
}

export default HeaderContent;