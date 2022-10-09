import { Suspense } from "react";

// import project component
import Loader from "./Loader";

// Loader - Lazy Load

const Loadable = (Component) => (props) => (
    <Suspense fallback={<Loader />}>
        <Component {...props}/>
    </Suspense>
)

export default Loadable;