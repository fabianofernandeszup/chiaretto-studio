arrAllFilesChanged=(/home/fabiano.fernandes/www/stackspot/chiaretto-studio/plugins/*)
arrAllDirs=()
# Check dir
for counter in ${!arrAllFilesChanged[*]}; do
  if [ -d "${arrAllFilesChanged[counter]}" ]; then
      arrAllDirs=(${arrAllDirs[@]} "${arrAllFilesChanged[counter]}")
  else
  	arrAllDirs=(${arrAllDirs[@]} "${arrAllFilesChanged[counter]%/*}")
  fi
done

echo "###### Filter Uniq Dir #########"
readarray -t arrAllDirs < <(printf '%s\n' "${arrAllDirs[@]}" | sort -u)

echo "###### Publish #########"
for i in ${arrAllDirs[@]}; do
  if [[ -f "${i}/plugin.yaml" ]]; then
    echo "cd $i"
    echo "stk publish plugin"
  fi
  if [[ -f "${i}/action.yaml" ]]; then
    echo "cd $i"
    echo "stk publish action"
  fi
done
