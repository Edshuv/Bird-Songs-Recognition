% written by Hong Yee Cheah

%split recording to smaller 3s recording
process='Anderson-serviceberry-selected' %recording folder name will be process for feature extration 
name=sprintf('\\%s',process);
name=dir(process);
[L,M]=size(name);

% feature extration for 3 second interval for each recording located in
% process and save the recording of 3 second inverval to split recording
% folder
for j=3:L%3:L
filename_o=name(j).name;
filename_o=sprintf('%s\\%s',process,filename_o);
[audioIn,fs] = audioread(filename_o);
xxx=sprintf('split_recording\\%s',filename_o(end-4-8:end-4));
mkdir(xxx);
subaudiosize=3*fs;
mfcc4s=[];
label=[];
for i=0:19
    y=audioIn((i*subaudiosize+1):((i+1)*subaudiosize));
    if i*3<10
       save=['0',num2str(i*3)] ;
    else
        save=num2str(i*3);
    end
    %save audio of each 3 second interval into a split recording and save
    %that in different file and arrange by the name
    filename=sprintf('split_recording\\%s\\%s_%s.WAV',filename_o(end-4-8:end-4),filename_o(end-4-8:end-4),save);
    audiowrite(filename,y,fs) 
    
    %%savemfcc and find mfcc and log power for 3 second interval audio file
    mfcc4s=[mfcc4s;mean(mfcc(y,fs))];

end
    %write the feature into a single csv for each audio with 3 second
    %interval 
    csvfilename=sprintf('csvsave\\data\\%s.csv',filename_o(end-4-7:end-4));
    csvwrite(csvfilename,mfcc4s);    
end