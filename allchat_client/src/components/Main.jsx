import { Route, Routes } from 'react-router-dom'
import Home from './Home'
import Room from './Room'

export default function Main () {
    return (
        <div className="main-content">
            <Routes>
                <Route path = "/" element = {<Home />}/>
                <Route path = '/room' element = {<Room />}/>
            </Routes>
        </div>
    )
}