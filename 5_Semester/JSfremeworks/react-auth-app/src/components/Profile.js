import React from 'react';

const Profile = ({ authenticated }) => {
  return (
    <div>
      {authenticated ? (
        <div>
          <h2>Profile</h2>
          <p>Welcome to the Profile page.</p>
        </div>
      ) : (
        <div>
          <h2>Profile</h2>
          <p>Please log in to view the Profile page.</p>
        </div>
      )}
    </div>
  );
};

export default Profile;
