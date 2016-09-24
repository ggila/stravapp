FROM ubuntu:16.04 

RUN apt-get update  # might use cache: won't work
RUN apt-get install -y git vim ack-grep python3 zsh tmux
RUN git clone https://github.com/ggila/config.git /home/config
RUN ln -s /home/config/zshrc /home/.zshrc
RUN ln -s /home/config/vimrc /home/.vimrc
RUN ln -s /home/config/tmux.conf /home/.tmux.conf
CMD zsh
