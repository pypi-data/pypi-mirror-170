if command -v ${package} &> /dev/null
then
    printf "Installing ${package} with pip...\n"
    pip install ${package} --user
fi
