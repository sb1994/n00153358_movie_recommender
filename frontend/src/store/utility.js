export const updateStateObject = (prevStateObject, updatedStateProperties) => {
  return {
    ...prevStateObject,
    ...updatedStateProperties
  }
}