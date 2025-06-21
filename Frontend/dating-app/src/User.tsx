import { useEffect, useState } from "react";

interface User {
    id: number;
    username: string;
}

// const user_0 : User  = {
//     userId: 0,
//     userName: ""
// }

function DisplayUsers() {
    const [users, setUsers] = useState<User[]>([]);


    useEffect(() => {
        fetch("http://localhost:8000/user/")
        .then(response => response.json())
        .then(data => setUsers(data))
    },[]);

    const listUsers = users.map(user =>
        <li key={user.id}>{user.id}: {user.username}</li>
     )

    return (
        <ul>{listUsers}</ul>
    )
}

export default DisplayUsers;