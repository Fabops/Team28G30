#!/bin/python3
Testing to create file remotely on git
To learn to fetch new files to our local environment
Learning new commands
We learn the git pull command
Using this to learn git fetch to fetch the changes in our remote repo.
# So everything above was done in the remote repos
We used git fetch G30/master to fetch the difference btwn our local repo and the remote repo
Using git fetch Alias/master instead of git pull ensures that all remote changes doesn't get merge directly into our local working environment, thus giving us the chance to review and approve the changes before mergeing with our local env
git fetch G30/master    git diff G30/master  REVIEW CHANGES if approve, git merge G30/master
We used git diff G30/master to view the diffference btw local and remote repos
Then used git merge G30/master to bring the changes once we approve.
Otherwise git pull will directly merge all the files from the remote repo to your local working area
#Now that we've finished documenting lcoally on the recently merged file, lets send it back to remote repo.
