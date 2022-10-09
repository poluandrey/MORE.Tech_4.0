import LocalGroceryStoreOutlinedIcon from '@mui/icons-material/LocalGroceryStoreOutlined';
import AccountCircleOutlinedIcon from '@mui/icons-material/AccountCircleOutlined';
import VideogameAssetOutlinedIcon from '@mui/icons-material/VideogameAssetOutlined';
import StarBorderOutlinedIcon from '@mui/icons-material/StarBorderOutlined';
import BusinessCenterOutlinedIcon from '@mui/icons-material/BusinessCenterOutlined';

const main = {
    id: 'main',
    title: '',
    type: 'group',
    children: [
        {
            id: 'my_task',
            type: 'item',
            title: 'Мои задачи',
            url: '/tasks',
            icon: BusinessCenterOutlinedIcon,
        },
        {
            id: 'liderboard',
            type: 'item',
            title: 'Лидербоард',
            url: '/liderboard',
            icon: StarBorderOutlinedIcon,
        },
        {
            id: 'game_zone',
            type: 'item',
            title: 'Игровое поле',
            url: '/game_zone',
            icon: VideogameAssetOutlinedIcon,
        },
        {
            id: 'profile',
            type: 'item',
            title: 'Мой профиль',
            url: '/profile',
            icon: AccountCircleOutlinedIcon,
        },
        {
            id: 'marketplace',
            type: 'item',
            title: 'Маркетплейс',
            url: '/marketplace',
            icon: LocalGroceryStoreOutlinedIcon,
        },
    ]
}

export default main;