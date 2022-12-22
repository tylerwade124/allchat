import { Route, Routes } from 'react-router-dom'
import Home from './Home'

export default function Main () {
    return (
        <div className="main-content">
            <Routes>
                <Route path = "/" element = {<Home />}/>
            </Routes>
        </div>
    )
}