import { Grid } from "@mui/material";
import CardTask from "../../components/cards/tasks/CardTask";

const MyTask = () => {

    return (
        <Grid container rowSpacing={4.5} columnSpacing={2.75}>
            <Grid item xs={12} sm={6} md={4} lg={3}>
                <CardTask />
            </Grid>
            <Grid item xs={12} sm={6} md={4} lg={3}>
                <CardTask />
            </Grid>
            <Grid item xs={12} sm={6} md={4} lg={3}>
                <CardTask />
            </Grid>
            <Grid item xs={12} sm={6} md={4} lg={3}>
                <CardTask />
            </Grid>
        </Grid>
    )
}

export default MyTask;