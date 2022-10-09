import SimpleBarScroll from "../../../../components/third/SimpleBar";
import Navigation from "./Navigation";

const DrawerContent = () => (
    <SimpleBarScroll
        sx={{
            '& .simplebar-content': {
                display: 'flex',
                flexDirection: 'column'
            }
        }}
    >
        <Navigation />
    </SimpleBarScroll>
)

export default DrawerContent;