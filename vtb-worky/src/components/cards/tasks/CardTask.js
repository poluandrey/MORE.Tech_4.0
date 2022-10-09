import { Avatar, Chip, Stack, Typography } from '@mui/material'
import PropTypes from 'prop-types'
import MainCard from '../../MainCard'
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';
import MessageOutlinedIcon from '@mui/icons-material/MessageOutlined';
import PushPinOutlinedIcon from '@mui/icons-material/PushPinOutlined';

const CardTask = () => {

    return (
        <MainCard contentSX={false} title=' '>
            <Stack spacing={0.5} direction='column'>

                <Stack direction='row' justifyContent='space-between'>
                    <Typography variant="h4" color="inherit">
                        Фильтрация
                    </Typography>
                    <MoreHorizIcon />
                </Stack>
                <Stack>
                    <Typography variant="h6" color="textSecondary">
                        Упростить для MVP
                    </Typography>
                </Stack>

                <Stack direction='row'>
                    <Chip
                        variant='combined'
                        size='small'
                        label={'Design'}
                        sx={{ borderRadius: '4px', background: '#3EA0E640' }}
                    >
                    </Chip>
                </Stack>

                <Stack direction='row' justifyContent='space-between' alignItems='center'>
                    <Stack direction='row' spacing={0.5}>
                        <PushPinOutlinedIcon sx={{ color: '#C4C4C4', rotate: '45deg' }}/>
                        <MessageOutlinedIcon sx={{ color: '#C4C4C4'}}/>
                        <Chip 
                            variant='outlined'
                            size='small'
                            label='18:00 25 Апр.'
                            color='success'
                            sx={{ borderRadius: '4px' }}
                        />
                    </Stack>
                    <Stack>
                        <Avatar />
                    </Stack>
                </Stack>
            </Stack>
        </MainCard>
    )
}

export default CardTask;