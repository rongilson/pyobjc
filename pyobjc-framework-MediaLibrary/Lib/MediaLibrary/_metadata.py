# This file is generated by objective.metadata
#
# Last update: Sun Aug 10 21:24:35 2014

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$MLApertureAllPhotosTypeIdentifier$MLApertureAllProjectsTypeIdentifier$MLApertureFacebookAlbumTypeIdentifier$MLApertureFacebookGroupTypeIdentifier$MLApertureFacesAlbumTypeIdentifier$MLApertureFlaggedTypeIdentifier$MLApertureFlickrAlbumTypeIdentifier$MLApertureFlickrGroupTypeIdentifier$MLApertureFolderAlbumTypeIdentifier$MLApertureLastImportAlbumTypeIdentifier$MLApertureLastNMonthsAlbumTypeIdentifier$MLApertureLastViewedEventAlbumTypeIdentifier$MLApertureLightTableTypeIdentifier$MLAperturePhotoStreamAlbumTypeIdentifier$MLAperturePlacesAlbumTypeIdentifier$MLAperturePlacesCityAlbumTypeIdentifier$MLAperturePlacesCountryAlbumTypeIdentifier$MLAperturePlacesPointOfInterestAlbumTypeIdentifier$MLAperturePlacesProvinceAlbumTypeIdentifier$MLApertureProjectAlbumTypeIdentifier$MLApertureProjectFolderAlbumTypeIdentifier$MLApertureRootGroupTypeIdentifier$MLApertureSlideShowTypeIdentifier$MLApertureSmugMugAlbumTypeIdentifier$MLApertureSmugMugGroupTypeIdentifier$MLApertureUserAlbumTypeIdentifier$MLApertureUserSmartAlbumTypeIdentifier$MLFinalCutEventCalendarGroupTypeIdentifier$MLFinalCutEventGroupTypeIdentifier$MLFinalCutEventLibraryGroupTypeIdentifier$MLFinalCutFolderGroupTypeIdentifier$MLFinalCutProjectGroupTypeIdentifier$MLFinalCutRootGroupTypeIdentifier$MLFolderGroupTypeIdentifier$MLFolderRootGroupTypeIdentifier$MLGarageBandFolderGroupTypeIdentifier$MLGarageBandRootGroupTypeIdentifier$MLLogicBouncesGroupTypeIdentifier$MLLogicProjectTypeIdentifier$MLLogicProjectsGroupTypeIdentifier$MLLogicRootGroupTypeIdentifier$MLMediaLoadAppFoldersKey$MLMediaLoadAppleLoops$MLMediaLoadExcludeSourcesKey$MLMediaLoadFoldersKey$MLMediaLoadIncludeSourcesKey$MLMediaLoadMoviesFolder$MLMediaLoadSourceTypesKey$MLMediaObjectAlbumKey$MLMediaObjectArtistKey$MLMediaObjectBitRateKey$MLMediaObjectChannelCountKey$MLMediaObjectCommentsKey$MLMediaObjectDurationKey$MLMediaObjectGenreKey$MLMediaObjectKeywordsKey$MLMediaObjectKindKey$MLMediaObjectProtectedKey$MLMediaObjectResolutionStringKey$MLMediaObjectSampleRateKey$MLMediaObjectTrackNumberKey$MLMediaSourceApertureIdentifier$MLMediaSourceAppDefinedFoldersIdentifier$MLMediaSourceCustomFoldersIdentifier$MLMediaSourceFinalCutIdentifier$MLMediaSourceGarageBandIdentifier$MLMediaSourceLogicIdentifier$MLMediaSourceMoviesFolderIdentifier$MLMediaSourcePhotoBoothIdentifier$MLMediaSourceiMovieIdentifier$MLMediaSourceiPhotoIdentifier$MLMediaSourceiTunesIdentifier$MLiMovieEventCalendarGroupTypeIdentifier$MLiMovieEventGroupTypeIdentifier$MLiMovieEventLibraryGroupTypeIdentifier$MLiMovieFolderGroupTypeIdentifier$MLiMovieProjectGroupTypeIdentifier$MLiMovieRootGroupTypeIdentifier$MLiPhotoAlbumTypeIdentifier$MLiPhotoEventAlbumTypeIdentifier$MLiPhotoEventsFolderTypeIdentifier$MLiPhotoFacebookAlbumTypeIdentifier$MLiPhotoFacebookGroupTypeIdentifier$MLiPhotoFacesAlbumTypeIdentifier$MLiPhotoFlaggedAlbumTypeIdentifier$MLiPhotoFlickrAlbumTypeIdentifier$MLiPhotoFlickrGroupTypeIdentifier$MLiPhotoFolderAlbumTypeIdentifier$MLiPhotoLastImportAlbumTypeIdentifier$MLiPhotoLastNMonthsAlbumTypeIdentifier$MLiPhotoLastViewedEventAlbumTypeIdentifier$MLiPhotoLibraryAlbumTypeIdentifier$MLiPhotoPhotoStreamAlbumTypeIdentifier$MLiPhotoPlacesAlbumTypeIdentifier$MLiPhotoPlacesCityAlbumTypeIdentifier$MLiPhotoPlacesCountryAlbumTypeIdentifier$MLiPhotoPlacesPointOfInterestAlbumTypeIdentifier$MLiPhotoPlacesProvinceAlbumTypeIdentifier$MLiPhotoRootGroupTypeIdentifier$MLiPhotoSlideShowAlbumTypeIdentifier$MLiPhotoSmartAlbumTypeIdentifier$MLiPhotoSubscribedAlbumTypeIdentifier$MLiTunesAudioBooksPlaylistTypeIdentifier$MLiTunesFolderPlaylistTypeIdentifier$MLiTunesGeniusPlaylistTypeIdentifier$MLiTunesMoviesPlaylistTypeIdentifier$MLiTunesMusicPlaylistTypeIdentifier$MLiTunesPlaylistTypeIdentifier$MLiTunesPodcastPlaylistTypeIdentifier$MLiTunesPurchasedPlaylistTypeIdentifier$MLiTunesRootGroupTypeIdentifier$MLiTunesSavedGeniusPlaylistTypeIdentifier$MLiTunesSmartPlaylistTypeIdentifier$MLiTunesTVShowsPlaylistTypeIdentifier$MLiTunesiTunesUPlaylistTypeIdentifier$'''
enums = '''$MLMediaSourceTypeAudio@1$MLMediaSourceTypeImage@2$MLMediaSourceTypeMovie@4$MLMediaTypeAudio@1$MLMediaTypeImage@2$MLMediaTypeMovie@4$'''
misc.update({})
expressions = {}

# END OF FILE