import MainLayout from "../layouts/MainLayouts";
import Loadable from "../components/Loadable";
import { lazy } from "react";

// render Task Page
const MyTask = Loadable(lazy(() => import('../pages/MyTask')))

const worky = {
    path: '/',
    element: <MainLayout />,
    children: [
        {
            path: 'tasks',
            element: <MyTask />,
        },
        {
            path: 'liderboard',
            element: <MyTask />,
        },
        {
            path: 'game_zone',
            element: <MyTask />,
        },
        {
            path: 'profile',
            element: <MyTask />,
        },
        {
            path: 'marketplace',
            element: <MyTask />,
        },
    ]
}

export default worky;